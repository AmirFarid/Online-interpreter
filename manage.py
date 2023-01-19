import unittest
from flask.cli import FlaskGroup
from project import app, db

cli = FlaskGroup(app)

@cli.command()
def test():
	""" Runs the tests without code coverage"""
	tests = unittest.TestLoader().discover('project/test', pattern='test*.py')
	result = unittest.TextTestRunner(verbosity=2).run(tests)
	if result.wasSuccessful():
		return 0
	return 1

@cli.command()
def recreatedb():
	db.drop_all()
	db.create_all()
	db.session.commit()

if __name__ == '__main__':
	cli()