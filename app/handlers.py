from app.modules.home import HomeHandler
from app.modules.examples.pipeline_example import PipelineExampleHandler
from app.modules.examples.http_example import HttpExampleHandler
from app.modules.examples.datastore_example import DatastoreExampleHandler
from app.modules.examples.yaml_example import YamlExampleHandler
from app.modules.training.pipeline_training import PipelineTrainigHandler
from app.modules.training.http_training import HttpTrainingHandler
from app.modules.training.datastore_training import DatastoreTrainingHandler
from app.modules.cityinfo.cityinfo import CityInfoBuildHandler
from app.modules.cityinfo.cityinfo import CityInfoViewHandler

def handlers():
    return [
        (r'/', HomeHandler),
        (r'/examples/pipeline', PipelineExampleHandler),
        (r'/examples/pipeline/(\d+)', PipelineExampleHandler),
        (r'/examples/http', HttpExampleHandler),
        (r'/examples/http/([\d\.]+)/([\d\.]+)', HttpExampleHandler),
        (r'/examples/datastore', DatastoreExampleHandler),
        (r'/examples/datastore/([^\/]+)', DatastoreExampleHandler),
        (r'/examples/datastore/([^\/]+)/([^\/]+)', DatastoreExampleHandler),
        (r'/examples/yaml', YamlExampleHandler),
        (r'/training/pipeline/(\d+)', PipelineTrainigHandler),
        (r'/training/http/([-?\d\.]+)/([-?\d\.]+)', HttpTrainingHandler),
        (r'/training/datastore', DatastoreTrainingHandler),
        (r'/cityinfo/build', CityInfoBuildHandler),
        (r'/cityinfo/view', CityInfoViewHandler),
    ]
