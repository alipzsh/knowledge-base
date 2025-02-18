# wordpress
* use `/auxiliary/scanner/http/wordpress-scanner` to scan the
  folder for vulnerabilities.

* find the version
  `
  target_endpoint="$url/wp-content/plugins/wp-file-manager/readme.
  txt"
  version=$( curl -ks --max-time 5 --user-agent "$user_agent"
  "$target_endpoint" | grep -A 5 "== Changelog ==" | grep -E -o
  "[0-9]\.[0-9]" | head -n 1 )
  `
* enumerate `wordpress/index.php`.
  `
