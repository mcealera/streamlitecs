import aws_cdk as core
import aws_cdk.assertions as assertions

from streamlitecs.streamlitecs_stack import StreamlitecsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in streamlitecs/streamlitecs_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = StreamlitecsStack(app, "streamlitecs")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
