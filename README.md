# Kumo Example

Make Funix work in AWS Elastic Beanstalk.

## Usage

Just download the repo zip and choose Python 3.11 platform in Elastic Beanstalk to deploy.

## Extra

If you need to deploy your Funix project to Elastic Beanstalk.

Please create a new `application.py` and add:

```python
from funix import get_flask_application

application = get_flask_application("main.py")  # Your funix project main file, and you can add start arguments in
                                                # `get_flask_application` like `funix.run`

if __name__ == "__main__":
    application.run()
```

Also create a new `.ebextensions` folder, create a new `python.config` in it:

```yaml
option_settings:
  "aws:elasticbeanstalk:container:python":
    WSGIPath: application:application
```

If the `WSGIPath` does not match the path of `funix_flask_application` in your project, please edit it yourself.

### Need plot or Git

Use `funix[plot]` in `requirements.txt` if your project need Matplotlib support.

For git, please add a new config file in `.ebextensions`:

```yaml
packages:
  yum:
    git: []
```

## Future

Kumo will do the above.
