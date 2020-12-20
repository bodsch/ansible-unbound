import pytest
import os
import yaml
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture()
def AnsibleDefaults():
    with open("../../defaults/main.yml", 'r') as stream:
        return yaml.load(stream)


@pytest.mark.parametrize("dirs", [
    "/etc/unbound",
    "/etc/unbound/unbound.conf.d",
])
def test_directories(host, dirs):
    d = host.file(dirs)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("files", [
    "/etc/unbound/unbound.conf",
    "/etc/unbound/unbound.conf.d/server.conf",
    "/etc/unbound/unbound.conf.d/forward_zone.conf",
    "/etc/unbound/unbound.conf.d/remote_control.conf",
    "/etc/unbound/unbound.conf.d/cache_db.conf",
])
def test_files(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file


def test_user(host):
    assert host.group("unbound").exists
    assert host.user("unbound").exists
    assert "unbound" in host.user("unbound").groups
    assert host.user("unbound").shell == "/usr/sbin/nologin"
    assert host.user("unbound").home == "/var/lib/unbound"


def test_service(host):
    service = host.service("unbound")
    assert service.is_enabled
    assert service.is_running


@pytest.mark.parametrize("ports", [
    '0.0.0.0:53',
    '127.0.0.1:8953',
])
def test_open_port(host, ports):

    for i in host.socket.get_listening_sockets():
        print(i)

    application = host.socket("tcp://%s" % (ports))
    assert application.is_listening
