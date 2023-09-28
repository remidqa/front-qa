# FRONT-QA

- this website is a based on the following project : [app-generator/jinja-black-dashboard](https://github.com/app-generator/jinja-black-dashboard). If you want to use the the template I recommand to clone the original project.
- A live version is available at : [front.remidqa.com](https://front.remidqa.com)

## Technologies
- python
- jinja template
- Docker
- remidqa quality workflow

## Build
- This website is designed for a Docker usage.
- To build simple run : ```docker build -t {tag-name} .```
- Then the image will be available on your local repository

## Dependencies
- This website have been customized from the original project
- It requires a connection to a BFF application to manage some content
- For deployment and testing, this repository uses the [remidqa/build-deploy-test](https://github.com/remidqa/qa-configurations/blob/main/.github/workflows/build-deploy-test.yml) quality workflow
