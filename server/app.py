from flask import Flask, make_response, jsonify
from config import app, db, api
from models import Project
from flask_restful import Resource, Api

class Projects(Resource):
    def get(self):

        projects = Project.query.all()
        projects_data = [project.to_dict() for project in projects]
        return make_response(jsonify(projects_data), 200)
    
class ProjectDel(Resource):
    
    def delete(self, project_id):
        projectdel = Project.query.get(project_id)
        if projectdel is None:
            return make_response(jsonify(error="Project was not found"), 404)
        
        db.session.delete(projectdel)
        db.session.commit()

        return make_response('', 204)

api.add_resource(Project, '/projects')
api.add_resource(Project, '/projectdel/<int:project_id')

if __name__ == '__main__':
    app.run()