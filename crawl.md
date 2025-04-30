
on the whole or maybe on an interesting subdomains spider for more info and parameters that
pass data.

`sub_domians | httpx | katana`


an example of the whole process:

use the results of httpx.

```

cat unique_subs_httpx | cut -d " " -f 1 | katana -o katana_urls  

cat unique_subs_httpx | cut -d " " -f 1 | gau --o gau_urls

cat katana_urls gaulu_urls | sort -u | uro > filtered_endpoints.txt

```

then you can filter it even more for specific stuff: `cat filtered_endpoints.txt | grep /api/`


- If you want to extract deep links or JS endpoints, add flags like:

```
cat unique_subs_httpx | katana -u - -jc -d 2 -silent
```
