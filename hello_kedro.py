"""Contents of hello_kedro.py"""
from kedro.io import DataCatalog, MemoryDataSet
from kedro.pipeline import node, Pipeline
from kedro.runner import SequentialRunner

# Prepare a data catalog
data_catalog = DataCatalog({"example_data": MemoryDataSet()})

# Prepare second node
def join_statements(greeting):
    return f"{greeting} Kedro!"


join_statements_node = node(
    join_statements, inputs="my_salutation", outputs="my_message"
)

# Prepare first node
def return_greeting():
    return "Bonjourno"


return_greeting_node = node(
    return_greeting, inputs=None, outputs="my_salutation"
)

# Assemble nodes into a pipeline
pipeline = Pipeline([join_statements_node, return_greeting_node])

# Create a runner to run the pipeline
runner = SequentialRunner()

# Run the pipeline
print(runner.run(pipeline, data_catalog))