# Syncany Cloudflare Source Plugin (`v1.0.0`)

CloudQuery-compatible **Cloudflare** source plugin for Syncany (`22` tables + single-flight API request cache + `7` automated security posture rules).

## Included Tables (22)

| Table | Parent | Columns | Description |
| :--- | :--- | :---: | :--- |
| `cloudflare_access_applications` | `cloudflare_accounts` | 29 | Cloudflare Zero Trust Access applications configured at account or zone level (CloudQuery cloudflare_access_applications) |
| `cloudflare_access_groups` | `cloudflare_accounts` | 15 | Cloudflare Zero Trust Access groups defining reusable include/exclude/require identity rules (CloudQuery cloudflare_access_groups) |
| `cloudflare_account_members` | `cloudflare_accounts` | 14 | Cloudflare account members, roles, MFA status, and access policies (CloudQuery cloudflare_account_members) |
| `cloudflare_account_rulesets` | `cloudflare_accounts` | 15 | Account-wide Cloudflare WAF, DDoS, and Magic Transit rulesets (CloudQuery cloudflare_account_rulesets) |
| `cloudflare_accounts` | — | 12 | Cloudflare accounts accessible to the API token (CloudQuery cloudflare_accounts) |
| `cloudflare_certificate_packs` | `cloudflare_zones` | 21 | Cloudflare Universal, Advanced, and Custom SSL/TLS certificate packs per zone (CloudQuery cloudflare_certificate_packs) |
| `cloudflare_custom_hostnames` | `cloudflare_zones` | 16 | Cloudflare for SaaS Custom Hostnames and SSL configuration per zone (CloudQuery cloudflare_custom_hostnames) |
| `cloudflare_dns_records` | `cloudflare_zones` | 27 | Cloudflare DNS records per zone with full proxy status, TTL, priority, tags, comments, and timestamps (CloudQuery cloudflare_dns_records) |
| `cloudflare_images` | `cloudflare_accounts` | 13 | Cloudflare Images stored in the account (CloudQuery cloudflare_images) |
| `cloudflare_page_rules` | `cloudflare_zones` | 14 | Cloudflare Page Rules per zone with URL targets, forwarding/cache/security actions, and priority (CloudQuery cloudflare_page_rules) |
| `cloudflare_security_findings` | `cloudflare_zones` | 25 | Automated Cloudflare security posture & root-cause audit findings with full evidence and remediation steps |
| `cloudflare_waf_groups` | `cloudflare_zones` | 16 | Cloudflare WAF rule groups inside each WAF package (CloudQuery cloudflare_waf_groups) |
| `cloudflare_waf_overrides` | `cloudflare_zones` | 15 | URI-based Cloudflare WAF overrides per zone (CloudQuery cloudflare_waf_overrides) |
| `cloudflare_waf_packages` | `cloudflare_zones` | 13 | Cloudflare WAF Managed Packages per zone (CloudQuery cloudflare_waf_packages) |
| `cloudflare_waf_rules` | `cloudflare_zones` | 17 | Individual Cloudflare WAF managed rules per package (CloudQuery cloudflare_waf_rules) |
| `cloudflare_worker_cron_triggers` | `cloudflare_accounts` | 10 | Scheduled Cron Triggers attached to Cloudflare Worker scripts (CloudQuery cloudflare_worker_cron_triggers) |
| `cloudflare_worker_meta_data` | `cloudflare_accounts` | 16 | Cloudflare Workers scripts deployed in the account (CloudQuery cloudflare_worker_meta_data) |
| `cloudflare_worker_routes` | `cloudflare_zones` | 11 | Cloudflare Workers URL route bindings per zone (CloudQuery cloudflare_worker_routes) |
| `cloudflare_zone_ruleset_rules` | `cloudflare_zones` | 23 | Individual firewall, WAF, DDoS, rate-limit, and transform rules inside each Cloudflare zone ruleset |
| `cloudflare_zone_rulesets` | `cloudflare_zones` | 17 | Cloudflare modern Rulesets Engine phases per zone (WAF Custom, WAF Managed, Rate Limiting, DDoS, Transform, Cache, Redirects) |
| `cloudflare_zone_settings` | `cloudflare_zones` | 14 | Cloudflare zone security, SSL/TLS, WAF, caching, and network settings (~56 settings per zone) |
| `cloudflare_zones` | — | 30 | Cloudflare DNS zones with full plan, owner, registrar, nameserver, and tenant metadata (CloudQuery cloudflare_zones) |
