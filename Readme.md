[![tests](https://github.com/boutetnico/ansible-role-logrotate/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-logrotate/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.logrotate-blue.svg)](https://galaxy.ansible.com/boutetnico/logrotate)

ansible-role-logrotate
======================

This role installs and configures logrotate.

Requirements
------------

Ansible 2.7 or newer.

Supported Platforms
-------------------

- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)

Role Variables
--------------

| Variable               | Required | Default             | Choices   | Comments                                 |
|------------------------|----------|---------------------|-----------|------------------------------------------|
| logrotate_dependencies | true     | `logrotate`         | string    |                                          |
| logrotate_scripts      | true     | `[]`                | list      |                                          |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-logrotate

          logrotate_scripts:
            - name: kibana
              path: /var/log/kibana/*.log
              options:
                - rotate 7
                - daily
                - missingok
                - notifempty
                - delaycompress
                - compress
                - copytruncate
                - create 0640 kibana kibana
            - name: php8.1-fpm
              path: /var/log/php8.1-fpm.log
              options:
                - rotate 7
                - daily
                - missingok
                - notifempty
                - delaycompress
                - compress
                - create 0640 root adm
              scripts:
                postrotate: /usr/lib/php/php8.1-fpm-reopenlogs


Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
