import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_python_present(host):
    assert host.run('test -e /usr/bin/python').rc == 0


def test_aur_builder_user_is_wheel(host):
    aur_user = host.user('aur_builder')
    assert 'wheel' in aur_user.groups


def test_aur_builder_sudo_access_pacman(host):
    sudo_file_path = '/etc/sudoers.d/11-install-aur_builder'
    visudo_check_cmd = 'visudo -cf ' + sudo_file_path
    with host.sudo():
        sudo_file = host.file(sudo_file_path)
        validation_cmd = host.run(visudo_check_cmd)
        assert sudo_file.user == 'root'
        assert validation_cmd.rc == 0
        assert 'OK' in validation_cmd.stdout
        assert sudo_file_path in validation_cmd.stdout


@pytest.mark.parametrize('cmd,rc', [
    ('curl --version', 0),
    ('wget --version', 0),
    ('git --version', 0),
])
def test_bootstrap_apps_run(host, cmd, rc):
    assert host.run(cmd).rc == rc


def test_aur_ansible_module_installed(host):
    aur_path = host.user().home + '/.ansible/plugins/modules/aur/aur.py'
    assert host.file(aur_path).exists
    assert host.file(aur_path).is_file


@pytest.mark.parametrize('pkg', ['binutils', 'make', 'gcc', 'fakeroot'])
def test_makepkg_dependencies_present(host, pkg):
    assert host.package(pkg).is_installed


def test_aur_helper_yay_runs(host):
    test_cmd = host.run('yay --version')
    assert test_cmd.rc == 0
    assert 'yay' in test_cmd.stdout
