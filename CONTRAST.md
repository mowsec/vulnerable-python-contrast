# Contrast Security - Python Flask Instrumentation

This repository is an example of how to install the Contrast Security Agent 
in a Python Flask application.

* Original vulnerable application source code taken from ::fork_and_knife:
[dolevf/Damn-Vulnerable-GraphQL-Application][DVGQA]
* Only changes made are to instrument the application with 
[Contrast Secuirty][Contrast Home]



## Instrument a python application with Contrast Security
A step-by-step guide for implementing the Agent in this specific application, 
instrumentation requirements vary per technology stack. Please refer to the 
official [Contrast Security Docuemntation][Contrast Docs Home] for more 
information.

#### 1. Install the Agent
The agent is installed as a package from PyPi and can be found 
[here](https://pypi.org/project/contrast-agent/). You can either install it 
manually using the `pip` command or by adding it to your project's 
`requirements.txt` or `setup.py` configuration.

```bash
pip install contrast-agent
```


#### 2. Provision middleware components
Wrap the Flask application `app` object with the Contrast Security Agent 
middleware component.

[1]: Damn-Vulnerable-GraphQL-Application/app.py
[:link: `Damn-Vulnerable-GraphQL-Application/app.py#9-13`:][1]
```python
...
import contrast
from contrast.flask import ContrastMiddleware       # <-- Import here

app = Flask(__name__, static_folder="static/")
app.wsgi_app = ContrastMiddleware(app)              # <-- Wrap middlewhere here
...
```

#### 3. Configure the Contrast Agent
Using the [YAML template][Configure agent] provided, or by downloading a YAML 
template from the Contrast web portal, we can configure the agent:

`contrast_security.yml`:
```yaml
api:
  url: https://eval.contrastsecurity.com/Contrast
  api_key: XXX
  service_key: XXX
  user_name: XXX@XXX

application:
    name: VulnerableApp-Python-Demo
    code: demo-3

agent:
  service:
    host: localhost
    port: 30555
```

> :warning: **Do not commit API credentials to your GitHub repo!**: A template 
`contrast_security.yml.dist` file has been provided for your convienience. Copy
this file to `contrast_security.yml` and add your API details. This file is 
already added to `.gitignore` - ensure you don't accedentally remove this or
add it anyway.

The Dockerfile in this repo adds this file into the build at the default 
location of `/opt/contrast/contrast_security.yaml`.


#### 4. Run your application
Now run your applciation and browse around the pages as you normally would. If 
everything worked, then when you next go to your Contrast Security dashboard 
you'll see details for the new application and any security issues that have
been detected.


## Resources used
A list of resources that I found particularly usefull when attempting this.
##### Contrast Documentation
* [Contrast Security Docuemntation][Contrast Docs Home]
    * [Agents -> Python agent][Python agent]
        * [Install the Python agent with PyPI][Install PyPi]
        * [Configure middleware (Flask)][Configure middleware]
        * [Configure the agent (YAML config)][Configure agent]

##### Further Reading
* https://github.com/Contrast-Security-OSS/vulnpy
* [dolevf/Damn-Vulnerable-GraphQL-Application][DVGQA]


[Contrast Home]: https://www.contrastsecurity.com/
[Contrast Docs Home]: https://docs.contrastsecurity.com/index.html?lang=en
[Python agent]: https://docs.contrastsecurity.com/en/python.html
[Install PyPi]: https://docs.contrastsecurity.com/en/install-python-with-pypi.html
[Configure middleware]: https://docs.contrastsecurity.com/en/python-middleware.html
[Configure agent]: https://docs.contrastsecurity.com/en/python-configuration.html
[DVGQA]: https://github.com/dolevf/Damn-Vulnerable-GraphQL-Application
