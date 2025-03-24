# Github Action to Azure Fn Demo
This repository is intended to serve as an instructional starting point for developing source-controlled Azure Python Functions with automated deployment actions.

This guide assumes a dual environment setup, `dev` and `prod`, which correspond to the git branches `dev` and `main`, respectively. Note that the terms "dev" and "test" may be used interchangably within this guide when not referring directly to git branches.

We will initially design the repository to support only a single function. Although efforts will be made to structure the workflow in a way to allow for multiple functions within this repository as a future enhancement. 

## Prerequisites
- Azure Function Creator permissions
- Visual Studio Code
- Python version between 3.0 and 3.11 (as of 03/25 3.12 is incompatible with some Microsoft Azure Libraries)
- A Github repository

## Project Structure
|-- hello-world (repository)
|   |__ .github
|       └── workflows
|           └── workflow.yml
|       └── actions
|           |__ hello-world-action
|               └── action.yml
|   |__ src
|       └── test-fn
|           └── 


## Azure resource configuration
- Create functions with naming scheme `[name]-fn-prod` and `[name]-fn-dev`
- Within `Deployment` tab of function creation flow, authorize Continuous Deployment for this repository
- Ensure `SCM Basic Auth Publishing` setting is enabled via `Settings > Configuration` menu
- From function home page, download publish profiles by clicking `Get publish profile` 

## Github Repository
### Branches
- `main` pushes to production fn and is the default github branch
- `dev` pushes to test fn and will need to be created upon repository initialization
### Upload publish profiles
Publish profiles for dev function and prod function


## Function app
See readme within function_home directory (`src/test_fn`) for details on basic azure function development.

## Continuous Integration via Github Actions
The 
