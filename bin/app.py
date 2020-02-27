import copy
from ariadne import QueryType, MutationType, graphql_sync, make_executable_schema
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify

type_defs = """

    type Student {
        name: String
    }

    type Class {
        name: String
    }

    type Query {
        hello: String!
        query_student(id: Int!): Student
        query_class(id : Int!): Class
    }

    type Mutation {
        create_student(name: String!): Student
        create_class(name: String!): Class
    }
"""

query = QueryType()
mutation = MutationType()

student = []
class_dict = []

@query.field("hello")
def resolve_hello(_, info):
    request = info.context
    user_agent = request.headers.get("User-Agent", "Guest")
    return "Hello, %s!" % user_agent

@query.field("query_student")
def resolve_query_student(*_, id):
    if len(student) > id:
        return student[id]
    return "Not found"

@mutation.field("create_student")
def resolve_create_student(*_, name):
    student.append({"name":name})
    return student[-1]

@query.field("query_class")
def resolve_query_class(*_, id):
    if len(class_dict) > id:
        return class_dict[id]
    return "Not found"

@mutation.field("create_class")
def resolve_create_class(*_, name):
    class_dict.append({"name":name})
    return class_dict[-1]

schema = make_executable_schema(type_defs, query, mutation)

app = Flask(__name__)


@app.route("/graphql", methods=["GET"])
def graphql_playgroud():
    # On GET request serve GraphQL Playground
    # You don't need to provide Playground if you don't want to
    # but keep on mind this will not prohibit clients from
    # exploring your API using desktop GraphQL Playground app.
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    # GraphQL queries are always sent as POST
    data = request.get_json()


    # Note: Passing the request to the context is optional.
    # In Flask, the current request is always accessible as flask.request
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code


if __name__ == "__main__":
    app.run(debug=True)