# install AWS SDK
pip install awscli
export PATH=$PATH:$HOME/.local/bin

# install necessary dependency for ecs-deploy
add-apt-repository ppa:eugenesan/ppa
apt-get update
apt-get install jq -y

# install ecs-deploy
curl https://raw.githubusercontent.com/silinternational/ecs-deploy/master/ecs-deploy | \
  sudo tee -a /usr/bin/ecs-deploy
sudo chmod +x /usr/bin/ecs-deploy

# login AWS ECR
eval $(aws ecr get-login --no-include-email)

# build the docker image and push to an image repository
docker build -t mattfemia/mattfemia-portfolio .
docker tag mattfemia/mattfemia-portfolio:latest $IMAGE_REPO_URL:latest
docker push $IMAGE_REPO_URL:latest

# update an AWS ECS service with the new image
ecs-deploy -c $CLUSTER_NAME -n $SERVICE_NAME -i $IMAGE_REPO_URL:latest --force-new-deployment --timeout 600