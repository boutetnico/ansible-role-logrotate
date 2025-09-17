[![tests](https://github.com/boutetnico/ansible-role-logrotate/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-logrotate/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.logrotate-blue.svg)](https://galaxy.ansible.com/boutetnico/logrotate)

ansible-role-logrotate
======================

This role installs and configures logrotate.

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)
- [Ubuntu - 24.04 (Noble Numbat)](http://releases.ubuntu.com/24.04/)

Role Variables
--------------

| Variable                   | Required | Default             | Choices   | Comments                                 |
|----------------------------|----------|---------------------|-----------|------------------------------------------|
| logrotate_dependencies     | true     | `logrotate`         | string    |                                          |
| logrotate_systemd_override | true     | `{}`                | dict      | Override logrotate systemd unit file.    |
| logrotate_scripts          | true     | `[]`                | list      |                                          |

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
            - name: php8.2-fpm
              path: /var/log/php8.2-fpm.log
              options:
                - rotate 7
                - daily
                - missingok
                - notifempty
                - delaycompress
                - compress
                - create 0640 root adm
              scripts:
                postrotate: /usr/lib/php/php8.2-fpm-reopenlogs


Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
