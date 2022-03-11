from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.trace.status import Status, StatusCode
from opentelemetry.sdk.resources import Resource
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)

#Define resource to identify our service
resource = Resource.create({"service.name": "InstructorPython"})

access_token = "<ACCESS_TOKEN>"

#configure initial tracer
provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(ConsoleSpanExporter())

OTLPProcessor =  BatchSpanProcessor(OTLPSpanExporter(
    endpoint:="https://ingest.lightstep.com/traces/otlp/v0.9",
    headers = (("lightstep-access-token", access_token),)
))

provider.add_span_processor(processor)
# provider.add_span_processor(OTLPProcessor)
trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)


def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will
    # repeat one time more than needed.
        with tracer.start_as_current_span("outerLoop"):   
            current_span = trace.get_current_span()
            current_span.set_attribute("outer iteration", i)
            if i > 10 :
                current_span.set_status(Status(StatusCode.ERROR))
                raise Exception("Array too large! Stop execution")
                break
                # Last i elements are already in place
            for j in range(0, n-i-1):
                with tracer.start_as_current_span("innerLoop"):
                    current_span = trace.get_current_span()
                    current_span.set_attribute("inner iteration", j)
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                    if arr[j] > arr[j + 1] :
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        current_span.add_event("swapLog", {
                            "inner iteration": j,
                            "log.severity": "event",
                            "log.message": "Swap occurred"
                            })
     
# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90, 100, 1231, 4213, 432, 33, 42, 62]
 
with tracer.start_as_current_span("parent"):
    current_span = trace.get_current_span()
    current_span.set_attribute("machineName", "InstructorMachine")
    current_span.set_attribute("owner", "#PythonInstrumentation")
    current_span.set_attribute("number", "4")
    try:
        bubbleSort(arr)
    except Exception as ex:
        current_span.record_exception(ex)
        current_span.set_status(Status(StatusCode.ERROR))


print ("Sorted array is:")
for i in range(len(arr)):
    print ("% d" % arr[i],end=" ")