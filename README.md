[![Build Status](https://www.travis-ci.com/mattfemia/mattfemia-portfolio.svg?branch=master)](https://www.travis-ci.com/mattfemia/mattfemia-portfolio)
[![codecov](https://codecov.io/gh/mattfemia/mattfemia-portfolio/branch/master/graph/badge.svg?token=HARA6tY145)](https://codecov.io/gh/mattfemia/mattfemia-portfolio)

# Matt Femia Web Application
  
Flask application used as a digital resume, staging application deployments, and for showing freelance clients mockups of their projects.  
  
## CI/CD & AWS Deployment Architecture

This app has a CI/CD deployment configuration using TravisCI and AWS:  
  
- First changes to the Master branch trigger travis-yaml script to initiate Docker image to push up to an existing repo on AWS ECR  
- Then change to ECR repo triggers the automated setup of new ECS Task Definition which phase into ECS service via its Auto-Scaling Group  
- Finally, the existing EC2 instances update  
  
## Main site application  
  
- Single-page Dockerized Flask application used as digital resume  
- Details about my education, experience, projects, publications, and more is found here  
- Application is hosted using AWS architecture and sits behind an application load balancer to route traffic to each subdomain  

## Project Routes
  
- [Clonotypr](https://www.mattfemia.com/clonotypr) - R package. Bioinformatics tools for analyzing and visualizing immunosequencing data  
- [Clonotypy](https://www.mattfemia.com/clonotypy) - Python package. Python version of clonotypr, with support for Scanpy and many additional statistical analysis.
  
## App Subdomains  

- [ImmunoVue](https://vue.mattfemia.com) - Python (Flask) version of ImmunoTools -- analysis dashboard for scVDJ-seq data
- [ImmunoTools](https://immuno.mattfemia.com) - R Shiny data dashboard application for analyzing single-cell immune repertoire data
- [Labstock](https://labstock.mattfemia.com) - Node JS inventory and lab-supply order-tracking application
- [Seqbase](https://seqbase.mattfemia.com/redoc) - Serverless API to both retrieve and query on metadata from NGS-based studies (e.g., RNAseq, VDJseq, ATACseq) from a manually-curated database of published data

## External Project Redirects
  
Majority of my personal projects are hosted on their own domains and closed-source. Below are a few apps shown on the site:  
  
- [Micrographer](https://www.themicrographer.com) - My dropship eCommerce business for selling microscope artwork [Status: 🏢 Complete]
