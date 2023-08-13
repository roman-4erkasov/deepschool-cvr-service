#  Multi Label Classification  (hw01)

## About

Service that sets tags for aerospace images.
Examples of tags for some images:
|Image                             |Tags                       |
|:--------------------------------:|:-------------------------:|
|![](/tests/images/train_11111.jpg)|"partly_cloudy", "primary" |
|![](/tests/images/train_11110.jpg)|"clear", "primary"         |


You can read the full set of the tags in "src/config.yml".

## System Requirements
|System  |Required                                   |
|:------:|:-----------------------------------------:|
|OS      |Ubuntu 22.04.1 LTS (Jammy Jellyfish)       |
|Python  |Python 3.8.16                              |
|make    |Must be installed, part of build-essentials|


## Get Started in Host OS
Follow the following steps:
1. If you wish, set `APP_PORT`.
1. `cd deepschool-cvr-service`
1. `make install`
1. `source venv/bin/activate`
1. Get the private key and run `make download_weights`
1. `make run_app`

## Get Started with Docker
Follow the following steps:
1. If you wish, set `APP_PORT`, `DOCKER_TAG`, `DOCKER_IMAGE`.
1. Set demo_host in deploy/ansible/inventiry.ini
1. Run ci/cd pipeline of ".gitlab-ci.yml" or run these commands from this file manually.


## Test the service
Commands:
 - For all tests `make run_all_tests`
 - For unit tests `make run_unit_tests`
 - For integration tests `make run_all_tests`
 - For coverage report `make generate_coverage_report`
 
## Static analysis
 - Linter `make lint`
 
## Building Docker Image
Just run command `make build`
 
