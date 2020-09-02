import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_4_1_1_1_auditd_package(host):
    assert host.package('auditd').is_installed


def test_4_1_1_1_audispd_plugins_package(host):
    assert host.package('audispd-plugins').is_installed


def test_4_1_1_2_auditd_service(host):
    assert host.service('auditd').is_enabled


def test_4_1_3_audit_rule_file_exists(host):
    assert host.file('/etc/audit/rules.d/4.1.3.rules').exists


def test_4_1_3_audit_rule_file_isfile(host):
    assert host.file('/etc/audit/rules.d/4.1.3.rules').is_file


def test_4_1_4_audit_rule_file_exists(host):
    assert host.file('/etc/audit/rules.d/4.1.4.rules').exists


def test_4_1_4_audit_rule_file_isfile(host):
    assert host.file('/etc/audit/rules.d/4.1.4.rules').is_file


def test_4_1_5_audit_rule_file_exists(host):
    assert host.file('/etc/audit/rules.d/4.1.5.rules').exists


def test_4_1_5_audit_rule_file_isfile(host):
    assert host.file('/etc/audit/rules.d/4.1.5.rules').is_file


def test_4_1_6_audit_rule_file_exists(host):
    assert host.file('/etc/audit/rules.d/4.1.6.rules').exists


def test_4_1_6_audit_rule_file_isfile(host):
    assert host.file('/etc/audit/rules.d/4.1.6.rules').is_file


def test_4_1_7_audit_rule_file_exists(host):
    assert host.file('/etc/audit/rules.d/4.1.7.rules').exists


def test_4_1_7_audit_rule_file_isfile(host):
    assert host.file('/etc/audit/rules.d/4.1.7.rules').is_file


def test_4_1_8_audit_rule_file_exists(host):
    assert host.file('/etc/audit/rules.d/4.1.8.rules').exists


def test_4_1_8_audit_rule_file_isfile(host):
    assert host.file('/etc/audit/rules.d/4.1.8.rules').is_file


def test_4_1_9_audit_rule_file_exists(host):
    assert host.file('/etc/audit/rules.d/4.1.9.rules').exists


def test_4_1_9_audit_rule_file_isfile(host):
    assert host.file('/etc/audit/rules.d/4.1.9.rules').is_file


def test_4_1_10_audit_rule_file_exists(host):
    assert host.file('/etc/audit/rules.d/4.1.10.rules').exists


def test_4_1_10_audit_rule_file_isfile(host):
    assert host.file('/etc/audit/rules.d/4.1.10.rules').is_file


def test_4_1_11_audit_rule_file_exists(host):
    assert host.file('/etc/audit/rules.d/4.1.11.rules').exists


def test_4_1_11_audit_rule_file_isfile(host):
    assert host.file('/etc/audit/rules.d/4.1.11.rules').is_file


def test_4_1_12_audit_rule_file_exists(host):
    assert host.file('/etc/audit/rules.d/4.1.12.rules').exists


def test_4_1_12_audit_rule_file_isfile(host):
    assert host.file('/etc/audit/rules.d/4.1.12.rules').is_file


def test_4_1_13_audit_rule_file_exists(host):
    assert host.file('/etc/audit/rules.d/4.1.13.rules').exists


def test_4_1_13_audit_rule_file_isfile(host):
    assert host.file('/etc/audit/rules.d/4.1.13.rules').is_file


def test_4_1_14_audit_rule_file_exists(host):
    assert host.file('/etc/audit/rules.d/4.1.14.rules').exists


def test_4_1_14_audit_rule_file_isfile(host):
    assert host.file('/etc/audit/rules.d/4.1.14.rules').is_file


def test_4_1_15_audit_rule_file_exists(host):
    assert host.file('/etc/audit/rules.d/4.1.15.rules').exists


def test_4_1_15_audit_rule_file_isfile(host):
    assert host.file('/etc/audit/rules.d/4.1.15.rules').is_file
