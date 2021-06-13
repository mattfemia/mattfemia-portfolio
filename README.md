[![Build Status](https://www.travis-ci.com/mattfemia/mattfemia-portfolio.svg?branch=master)](https://www.travis-ci.com/mattfemia/mattfemia-portfolio)
[![codecov](https://codecov.io/gh/mattfemia/mattfemia-portfolio/branch/master/graph/badge.svg?token=WKDI6ZLK0I)](https://codecov.io/gh/mattfemia/mattfemia-portfolio)

# Matt Femia Web Application
  
Flask application used as a digital resume, staging application deployments, and for showing freelance clients mockups of their projects.  
  
## CI/CD & AWS Deployment Architecture

This app has a CI/CD deployment configuration using TravisCI and AWS:  
  
- First changes to the Master branch trigger Docker image to push up to an existing repo on AWS ECR  
- Then changes to $IMAGE_REPO:latest on ECR trigger automated setup of new ECS Task Definition
- Finally, the existing EC2 instances on the ECS cluster push updates through the Auto-Scaling Group on the Application Load Balancer  

## Main site application  
  
- Single-page Dockerized Flask application used as digital resume  
- Details about my education, experience, projects, publications, and more is found here  
- Application is hosted using AWS architecture and sits behind an application load balancer to route traffic to each subdomain

## Project Routes
  
- [Clonotypr](http://www.mattfemia.com/clonotypr) - R package. Bioinformatics tools for analyzing and visualizing immunosequencing data  
  
## App Subdomains  
  
- [Labstock](http://labstock.mattfemia.com) - Node JS inventory and lab-supply order-tracking application
- [ImmunoTools](http://immuno.mattfemia.com) - R Shiny data dashboard application for analyzing single-cell immune repertoire data

## External Project Redirects
  
Majority of my personal projects are hosted on their own domains and closed-source. Below are a few apps shown on the site:  
  
- [Micrographer](https://www.themicrographer.com) - my dropship eCommerce business for selling microscope artwork [Status: 🏢 Complete]
- [LabVivo](https://www.labvivo.com) - my SaaS business offering a cloud-based software suite for lab research [Status: 🚧 In-Development]
- [ImmunoVue](https://www.immunovue.com) - API and database I developed for aggregating RepSeq/AIRR-seq/VDJ-seq data [Status: 🚧 In-Development]
