# Results

## Instructions

Clone this repo: https://github.com/da667/dalton/ at tag `patch-1` (commit
9ca87f0)

```bash
docker compose build
docker compose up
```

Use the web interface `http://localhost` to run pcaps through Snort and Suricata.

Running the Snort jobs requires modifying the snort configuration file (via the
web interface). Set the HOME_NET variable to include localhost `127.0.0.1/32`.

## PCAP Stats

| File | Requests |
| ---- | -------- |
| anomalousTrafficTest.pcap   | 24667 |
| normalTrafficTest.pcap      | 35999 |
| normalTrafficTraining.pcap  | 35999 |

## Results

| Program    | Version     | Ruleset                                 | File                          | Alerts |
| ---------- | ----------- | --------------------------------------- | ----------------------------- | ------ |
| Snort      | 2.9.15.1    | ET-20240422-all-snort.rules             | anomalousTrafficTest.pcap     | 1664 |
| Snort      | 2.9.18.1    | ET-20240422-all-snort.rules             | anomalousTrafficTest.pcap     | 1664 |
| Suricata   | 5.0.7       | ET-20240422-all-suricata.rules          | anomalousTrafficTest.pcap     | 1081 |
| Suricata   | 7.0.4       | ET-20240422-all-suricata.rules          | anomalousTrafficTest.pcap     | 1081 |
|  |  |  |  |  |
| Snort      | 2.9.15.1    | ET-20240422-all-snort.rules             | normalTrafficTest.pcap        | 5 |
| Snort      | 2.9.18.1    | ET-20240422-all-snort.rules             | normalTrafficTest.pcap        | 5 |
| Suricata   | 5.0.7       | ET-20240422-all-snort.rules             | normalTrafficTest.pcap        | 5 |
| Suricata   | 7.0.4       | ET-20240422-all-snort.rules             | normalTrafficTest.pcap        | 5 |
|  |  |  |  |  |
| Snort      | 2.9.15.1    | ET-20240422-all-snort.rules             | normalTrafficTraining.pcap    | 0 |
| Snort      | 2.9.18.1    | ET-20240422-all-snort.rules             | normalTrafficTraining.pcap    | 0 |
| Suricata   | 5.0.7       | ET-20240422-all-snort.rules             | normalTrafficTraining.pcap    | 0 |
| Suricata   | 7.0.4       | ET-20240422-all-snort.rules             | normalTrafficTraining.pcap    | 0 |
|  |  |  |  |  |
|  |  |  |  |  |
| Snort      | 2.9.18.1    | ET+community.rules (v2.9)               | anomalousTrafficTest.pcap     | 1664 |
| Suricata   | 7.0.4       | ET+travisbgreen/hunting-rules (8b07887) | anomalousTrafficTest.pcap     | 1089 |
|  |  |  |  |  |
| Snort      | 2.9.18.1    | ET+community.rules (v2.9)               | normalTrafficTest.pcap        | 5 |
| Suricata   | 7.0.4       | ET+travisbgreen/hunting-rules (8b07887) | normalTrafficTest.pcap        | 9 |
|  |  |  |  |  |
| Snort      | 2.9.18.1    | ET+community.rules (v2.9)               | normalTrafficTraining.pcap    | 0 |
| Suricata   | 7.0.4       | ET+travisbgreen/hunting-rules (8b07887) | normalTrafficTraining.pcap    | 4 |
