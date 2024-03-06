
## Streamlit on ECS 

This is a simple project showcasing Streamlit (https://streamlit.io/) on ECS using CDK dployment with Python.
It contains the Dockerfile required to build the container image and the CDK code to deploy the code on AWS. 
The CDK will create the ECS cluster, an Application Loadbalancer and a CloudFront distribution.

### Create the Docker image and push it to a repository.

1. You will need Docker enginer installed to create the image. See Docker installation guide here: https://docs.docker.com/engine/install/#server
Ensure you have Docker engine installed by running the `hello-world` Docker image:

```
sudo docker run hello-world
```

2. Navigate to the `streamlit` directory and build the Streamlit container image:

```
docker build -t streamlit .
```

You can test the container locally using:

```
docker run -p 80:80 streamlit
```

3. Push the image to a container repository. You can find a guide on how to create and push images to public ECR repository here:
https://docs.aws.amazon.com/AmazonECR/latest/public/public-repository-create.html

Alternatively you can use the pre-defined repository, but keep in mind this may contain an outdated image. It's recommended that you build your own container image.

5. Update the container image repository URL on line 40 in `streamlitecs/streamlitecs_stack.py` 

### Prepare and run the CDK app

Note that you will need a valid AWS cli profile. If you need to configure a profile, follow the instructions here:
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

1. To manually create a virtualenv on MacOS and Linux, navigate to the projects root directory and run:

```
$ python3 -m venv .venv
```

2. After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

3. Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

4. At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

5. If you need to bootstrap your CDK environment, do so now:

```
$ cdk bootstrap
```
  
5. You can now deploy the CloudFormation template for this code. You will need to have valid AWS profile configured - see 

```
$ cdk deploy
```

6. To delete all resources provisoned use:

```
$ cdk destroy
```


## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

