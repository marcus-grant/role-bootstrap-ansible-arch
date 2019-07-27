import os

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

def test_curl_installed(host):
    assert host.run('curl --version').rc == 0

def test_curl_installed(host):
    assert host.run('wget --version').rc == 0

# def test_aur_ansible_module_installed(host):
#     f = host.file('~/.ansible/plugins/modules/aur')
#     assert f.exists
