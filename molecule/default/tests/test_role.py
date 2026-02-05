import pytest


@pytest.mark.parametrize(
    "name",
    [
        ("logrotate"),
    ],
)
def test_dependencies_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


def test_logrotate_command_is_available(host):
    cmd = host.run("logrotate --version")
    assert cmd.rc == 0


@pytest.mark.parametrize(
    "file,user,group,mode",
    [
        ("kibana", "root", "root", 0o644),
    ],
)
def test_logrotate_scripts_exist(host, file, user, group, mode):
    script = host.file("/etc/logrotate.d/" + file)
    assert script.exists
    assert script.is_file
    assert script.user == user
    assert script.group == group
    assert script.mode == mode


def test_logrotate_directory_exists(host):
    directory = host.file("/etc/logrotate.d")
    assert directory.exists
    assert directory.is_directory
