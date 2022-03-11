from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
<<<<<<< Updated upstream
from opentelemetry.trace.status import Status, StatusCode
=======
>>>>>>> Stashed changes
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)

#Define resource to identify our service
resource = Resource.create({"service.name": "basic_service"})

access_token = "MY_TOKEN"

#configure initial tracer
provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(ConsoleSpanExporter())

OTLPProcessor =  BatchSpanProcessor(OTLPSpanExporter(
    endpoint = "https://ingest.lightstep.com:443/traces/otlp/v0.9",
    headers = (("lightstep-access-token", access_token),)
))

#configure initial tracer
provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)
provider.add_span_processor(OTLPProcessor)
trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)


def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will
    # repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

with tracer.start_as_current_span("root"):
    bubbleSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
    print ("% d" % arr[i],end=" ")