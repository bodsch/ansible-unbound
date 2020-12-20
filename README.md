
install and configure unbound

## default vars

```
unbound_config_defaults:
  server:
    verbosity: 1
    statistics-interval: 240
    use-syslog: "no"
    log-queries: "yes"
    logfile: /var/log/unbound.log
    num-threads: 1
    directory: "/etc/unbound"
    interface: 0.0.0.0
    do-ip4: 'yes'
    do-ip6: 'no'
    do-udp: 'yes'
    do-tcp: 'yes'
    access-control:
      - '127.0.0.0/8 allow'
    cache-min-ttl: 5
    cache-max-negative-ttl: 60
    root-hints: "/etc/unbound/root.hints"
    hide-identity: 'yes'
    hide-version: 'yes'
    prefetch: 'yes'
    max-udp-size: 4096
    msg-buffer-size: 65552
    unwanted-reply-threshold: 10000
    ipsecmod-enabled: 'no'


  forward_zone:
    name: "."
    # definitely censor free & log free with DNSSEC Support:
    forward_addrs:
      - 84.200.69.80   # DNS Watch
      - 84.200.70.40   # DNS Watch
      - 77.109.148.136 # Xiala.net
      - 77.109.148.137 # Xiala.net
      - 91.239.100.100 # censurfridns.dk
      - 89.233.43.71   # censurfridns.dk

  remote_control:
    server-key-file: "{{ unbound_conf_dir }}/unbound_server.key"
    server-cert-file: "{{ unbound_conf_dir }}/unbound_server.pem"
    control-key-file: "{{ unbound_conf_dir }}/unbound_control.key"
    control-cert-file: "{{ unbound_conf_dir }}/unbound_control.pem"

  certs:
    server:
      key_file: "{{ unbound_conf_dir }}/unbound_server.key"
      cert_file: "{{ unbound_conf_dir }}/unbound_server.pem"
    control:
      key_file: "{{ unbound_conf_dir }}/unbound_control.key"
      cert_file: "{{ unbound_conf_dir }}/unbound_control.pem"

  cachedb: {}

```
