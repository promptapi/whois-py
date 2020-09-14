![Python](https://img.shields.io/badge/python-3.7.4-green.svg)
![Version](https://img.shields.io/badge/version-0.0.0-orange.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Build Status](https://travis-ci.org/promptapi/whois-py.svg?branch=main)](https://travis-ci.org/promptapi/whois-py)

# Prompt API - Whois API - Python Package

`pa-whois` is a python wrapper for [whois api][whois-api]

## Requirements

1. You need to signup for [Prompt API][promptapi-signup]
1. You need to subscribe [whois api][whois-api], test drive is **free!!!**
1. You need to set `PROMPTAPI_TOKEN` environment variable after subscription.

then;

```bash
$ pip install pa-whois
```

---

## Example Usage

Let’s try with `check` endpoint:

```python
from whois import Whois

who = Whois()
who.check('promptapi.com')
# returns dict
# {'result': 'registered', 'status': 200}

# or
check_result = who.check('promptapi.com')
print(check_result)
# {'result': 'registered', 'status': 200}

who.check('promptapi.comaaaaaaaaaaaaaaaa')
# {'error': 'TLD not supported', 'status': 400}

who.check('promptapi-testing-domain.com') 
# {'result': 'available', 'status': 200}
```

Now, let’s try with `query` endpoint:

```python
from whois import Whois

who = Whois()
who.query('promptapi-testing-domain.com')
# {'error': 'No match for promptapi-testing-domain.com', 'status': 404}

who.query('promptapi.com')
#{'result': {'domain_name': 'PROMPTAPI.COM',
#  'registrar': 'NameCheap, Inc.',
#  'whois_server': 'whois.namecheap.com',
#  'referral_url': None,
#  'updated_date': '2020-05-27 22:19:36',
#  'creation_date': '2020-04-19 15:11:52',
#  'expiration_date': '2021-04-19 15:11:52',
#  'name_servers': ['APOLLO.NS.CLOUDFLARE.COM', 'MARJORY.NS.CLOUDFLARE.COM'],
#  'status': 'clientTransferProhibited https://icann.org/epp#clientTransferProhibited',
#  'emails': 'abuse@namecheap.com',
#  'dnssec': 'unsigned',
#  'name': None,
#  'org': None,
#  'address': None,
#  'city': None,
#  'state': None,
#  'zipcode': None,
#  'country': None},
# 'status': 200}
```

---

## License

This project is licensed under MIT

---

## Contributer(s)

* [Prompt API](https://github.com/promptapi) - Creator, maintainer

---

## Contribute

All PR’s are welcome!

1. `fork` (https://github.com/promptapi/whois-py/fork)
1. Create your `branch` (`git checkout -b my-feature`)
1. `commit` yours (`git commit -am 'Add awesome features...'`)
1. `push` your `branch` (`git push origin my-feature`)
1. Than create a new **Pull Request**!

This project is intended to be a safe,
welcoming space for collaboration, and contributors are expected to adhere to
the [code of conduct][coc].


---

[whois-api]:        https://promptapi.com/marketplace/description/whois-api
[promptapi-signup]: https://promptapi.com/#signup-form
[coc]:              https://github.com/promptapi/whois-py/blob/main/CODE_OF_CONDUCT.md
