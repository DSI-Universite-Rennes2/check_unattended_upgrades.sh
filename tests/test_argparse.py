from argparse import ArgumentParser, Namespace

import check_unattended_upgrades
from check_unattended_upgrades import get_argparser
from tests.helper import run


class TestWithSubprocess:
    def test_help(self) -> None:
        process = run(["--help"])
        assert process.returncode == 3
        assert "usage: check_unattended_upgrades" in process.stdout

    def test_version(self) -> None:
        process = run(
            ["--version"],
        )
        assert process.returncode == 3
        assert (
            "check_unattended_upgrades " + check_unattended_upgrades.__version__
            in process.stdout
        )


parser: ArgumentParser = get_argparser()


def args(*args: str) -> Namespace:
    return parser.parse_args(args)


class TestMethod:
    class TestWarning:
        def test_int(self) -> None:
            assert args("--warning", "42").warning == 42

        def test_timespan(self) -> None:
            assert args("--warning", "1s1m").warning == 61

    class TestCritical:
        def test_int(self) -> None:
            assert args("--critical", "123").critical == 123

        def test_critical_timespan(self) -> None:
            assert args("--critical", "1 min").critical == 60

    class TestVerbose:
        def test_zero(self) -> None:
            assert args().verbose == 0

        def test_one(self) -> None:
            assert args("-v").verbose == 1

        def test_two(self) -> None:
            assert args("-vv").verbose == 2

        def test_three(self) -> None:
            assert args("-vvv").verbose == 3
