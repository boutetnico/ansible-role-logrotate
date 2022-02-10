import pytest

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
  ('logrotate'),
])
def test_packages_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize('file', [
  ('kibana.conf'),
])
def test_cron_files_exist(host, file):
    cron_file = host.file('/etc/logrotate.d/' + file)
    assert cron_file.exists
    assert cron_file.is_file
    assert cron_file.user == 'root'
    assert cron_file.group == 'root'
