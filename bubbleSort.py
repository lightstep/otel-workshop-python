from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)

#Define resource to identify our service
resource = Resource.create({"service.name": "basic_service"})

#configure initial tracer
provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)

def bubble_sort(data):
    for _ in range(len(data)):
        with tracer.start_as_current_span("outerLoop"):
            for i in range(len(data) - 1):
                with tracer.start_as_current_span("innerLoop"):
                    if data[i] > data[i + 1]:
                        data[i], data[i + 1] = data[i + 1], data[i]
        return data

a_list = [2, 1, 5, 4, 3, 7, 1]

with tracer.start_as_current_span("root"):
    sorted_list = bubble_sort(a_list)

print(sorted_list)