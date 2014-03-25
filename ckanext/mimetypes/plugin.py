import mimetypes
import ckan.plugin as plugins

class MIMETypesPlugin(p.SingletonPlugin):
  p.implements(p.IConfigurer)

  def update_config(self, config):
    mimetypes.add_type('text/turtle', '.ttl')
    mimetypes.add_type('text/n3', '.n3')
    mimetypes.add_type('application/ld+json', '.jsonld')
    mimetypes.add_type('application/json', '.geojson')
