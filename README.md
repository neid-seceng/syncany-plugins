# Syncany Public Plugin Registry (`syncany-plugins`)

Official public plugin registry and SHA-256 verified artifact index for **Syncany**.

## Available Source Plugins

| Plugin | Latest Version | Protocol | Tables | Package Directory | Verified Archive (`.tar.gz`) |
| :--- | :---: | :---: | :---: | :--- | :--- |
| **`cloudflare`** | `v1.1.0` (`v1.0.0`) | `native` | **22** | [`cloudflare/v1.1.0/`](./cloudflare/v1.1.0/) | [`dist/cloudflare-v1.1.0.tar.gz`](./dist/cloudflare-v1.1.0.tar.gz) |
| **`aws`** | `v1.2.0` | `native` | **18** | [`aws/v1.2.0/`](./aws/v1.2.0/) | [`dist/aws-v1.2.0.tar.gz`](./dist/aws-v1.2.0.tar.gz) |
| **`plesk`** | `v1.0.0` | `yaml` | **4** | [`plesk/v1.0.0/`](./plesk/v1.0.0/) | [`dist/plesk-v1.0.0.tar.gz`](./dist/plesk-v1.0.0.tar.gz) |
| **`github`** | `v1.0.0` | `yaml` | **2** | [`github/v1.0.0/`](./github/v1.0.0/) | [`dist/github-v1.0.0.tar.gz`](./dist/github-v1.0.0.tar.gz) |
| **`example-python`** | `v1.0.0` | `subprocess` | **1** | [`example-python/v1.0.0/`](./example-python/v1.0.0/) | [`dist/example-python-v1.0.0.tar.gz`](./dist/example-python-v1.0.0.tar.gz) |

## Registry Endpoint

- **Index URL:** `https://raw.githubusercontent.com/neid-seceng/syncany-plugins/main/registry.json`

## 3-Tier Resolution Architecture

1. **Tier 1 (Warm Lambda Cache):** `/tmp/plugins/<plugin>/<version>/` (`0ms` network overhead on warm invocations).
2. **Tier 2 (Client S3 Mirror Cache):** `s3://<client-bucket>/_plugins/<plugin>/<version>.tar.gz` (same-region AWS S3 read + SHA-256 verification).
3. **Tier 3 (Remote GitHub Registry):** Downloads once per new version from `https://raw.githubusercontent.com/neid-seceng/syncany-plugins/main/dist/<plugin>-<version>.tar.gz`, verifies its SHA-256 digest against `registry.json`, mirrors into Tier 2 (`s3://<client-bucket>/_plugins/`), and extracts into Tier 1 (`/tmp/plugins/`).

## CLI Usage

```bash
# Pull and verify any plugin from the public registry
syncany plugin-pull cloudflare --version v1.1.0
syncany plugin-pull aws --version v1.2.0
syncany plugin-pull github --version v1.0.0
syncany plugin-pull plesk --version v1.0.0
syncany plugin-pull example-python --version v1.0.0
```
