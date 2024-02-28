
import os

root_dir = "out"

# Create the project folder
os.makedirs(root_dir, exist_ok=True)

# Create the backend folder
backend_dir = os.path.join(root_dir, "backend")
os.makedirs(backend_dir, exist_ok=True)

# Create the api folder
api_dir = os.path.join(backend_dir, "api")
os.makedirs(api_dir, exist_ok=True)

# Create the auth, recipes, and users folders
auth_dir = os.path.join(api_dir, "auth")
os.makedirs(auth_dir, exist_ok=True)
recipes_dir = os.path.join(api_dir, "recipes")
os.makedirs(recipes_dir, exist_ok=True)
users_dir = os.path.join(api_dir, "users")
os.makedirs(users_dir, exist_ok=True)

# Create the config, models, routes, services, and utils folders
config_dir = os.path.join(backend_dir, "config")
os.makedirs(config_dir, exist_ok=True)
models_dir = os.path.join(backend_dir, "models")
os.makedirs(models_dir, exist_ok=True)
routes_dir = os.path.join(backend_dir, "routes")
os.makedirs(routes_dir, exist_ok=True)
services_dir = os.path.join(backend_dir, "services")
os.makedirs(services_dir, exist_ok=True)
utils_dir = os.path.join(backend_dir, "utils")
os.makedirs(utils_dir, exist_ok=True)

# Create the frontend folder
frontend_dir = os.path.join(root_dir, "frontend")
os.makedirs(frontend_dir, exist_ok=True)

# Create the components, containers, pages, redux, and styles folders
components_dir = os.path.join(frontend_dir, "components")
os.makedirs(components_dir, exist_ok=True)
containers_dir = os.path.join(frontend_dir, "containers")
os.makedirs(containers_dir, exist_ok=True)
pages_dir = os.path.join(frontend_dir, "pages")
os.makedirs(pages_dir, exist_ok=True)
redux_dir = os.path.join(frontend_dir, "redux")
os.makedirs(redux_dir, exist_ok=True)
styles_dir = os.path.join(frontend_dir, "styles")
os.makedirs(styles_dir, exist_ok=True)

# Create the database folder
database_dir = os.path.join(root_dir, "database")
os.makedirs(database_dir, exist_ok=True)

# Create the cloud folder
cloud_dir = os.path.join(root_dir, "cloud")
os.makedirs(cloud_dir, exist_ok=True)

# Create the aws and azure folders
aws_dir = os.path.join(cloud_dir, "aws")
os.makedirs(aws_dir, exist_ok=True)
azure_dir = os.path.join(cloud_dir, "azure")
os.makedirs(azure_dir, exist_ok=True)

# Create the documentation folder
documentation_dir = os.path.join(root_dir, "documentation")
os.makedirs(documentation_dir, exist_ok=True)

# Create the testing folder
testing_dir = os.path.join(root_dir, "testing")
os.makedirs(testing_dir, exist_ok=True)

# Create the unit, integration, and e2e folders
unit_dir = os.path.join(testing_dir, "unit")
os.makedirs(unit_dir, exist_ok=True)
api_unit_dir = os.path.join(unit_dir, "api")
os.makedirs(api_unit_dir, exist_ok=True)
components_unit_dir = os.path.join(unit_dir, "components")
os.makedirs(components_unit_dir, exist_ok=True)
integration_dir = os.path.join(testing_dir, "integration")
os.makedirs(integration_dir, exist_ok=True)
e2e_dir = os.path.join(testing_dir, "e2e")
os.makedirs(e2e_dir, exist_ok=True)

# Create the build folder
build_dir = os.path.join(root_dir, "build")
os.makedirs(build_dir, exist_ok=True)

# Create the backend and frontend dist folders
backend_dist_dir = os.path.join(build_dir, "backend", "dist")
os.makedirs(backend_dist_dir, exist_ok=True)
frontend_dist_dir = os.path.join(build_dir, "frontend", "dist")
os.makedirs(frontend_dist_dir, exist_ok=True)

# Create the .env, package.json, .gitignore, and README.md files
env_file = os.path.join(root_dir, ".env")
with open(env_file, "w") as f:
    f.write("")

package_json_file = os.path.join(root_dir, "package.json")
with open(package_json_file, "w") as f:
    f.write("")

gitignore_file = os.path.join(root_dir, ".gitignore")
with open(gitignore_file, "w") as f:
    f.write("")

readme_file = os.path.join(root_dir, "README.md")
with open(readme_file, "w") as f:
    f.write("")
