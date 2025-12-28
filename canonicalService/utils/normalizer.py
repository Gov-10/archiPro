KNOWN_COMPONENTS = {
    "redis": "cache",
    "postgres": "database",
    "postgresql": "database",
    "mysql": "database",
    "api": "api",
    "fastapi": "api",
    "django": "api",
    "sqs": "queue",
    "rabbitmq": "queue",
    "pubsub": "queue",
    "s3": "object_storage",
    "frontend": "frontend",
    "nextjs": "frontend",
    "reactjs" : "frontend",
    "expressjs" : "api",
    "nestjs" : "api",
    "mongodb" : "database", 
    "springboot" : "api"
}

def normalize(text: str):
    components = []
    for line in text.lower().splitlines():
        for key, ctype in KNOWN_COMPONENTS.items():
            if key in line:
                components.append({"name": key, "type": ctype})
    return components

