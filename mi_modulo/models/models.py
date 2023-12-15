# models.py
from odoo import models, fields, api

class EmpresaContratista(models.Model):
    _name = 'empresa_contratista'
    _description = 'Empresas Contratistas'

    name = fields.Char(string='Nombre', required=True)
    direccion = fields.Char(string='Direccion', required=True)
    display_info = fields.Char(string='Display Info', compute='_compute_display_info')

    @api.depends('name', 'direccion')
    def _compute_display_info(self):
        for record in self:
            record.display_info = "{} - {}".format(record.name, record.direccion)

    # proyectos_ids = fields.One2many('project.project', 'contratista_id', string='Proyectos')
 
# class Proyecto(models.Model):
#     _name = 'project.project'
#     _inherit = 'project.project'

#     name = fields.Char(string='Campo', required=True)
    # contratista_id = fields.Many2one('mi_modulo.empresa_contratista', string='Contratista')
    # tareas_ids = fields.One2many('mi_modulo.tarea', 'proyecto_id', string='Tareas')
    # total_tareas = fields.Integer(string='Total de Tareas', compute='_compute_total_tareas', store=True)
    
    # @api.depends('tareas_ids')
    # def _compute_total_tareas(self):
    #     for proyecto in self:
    #         proyecto.total_tareas = len(proyecto.tareas_ids)

# class Tarea(models.Model):
#     _name = 'mi_modulo.tarea' 
#     _description = 'Tareas'
#     _inherit = 'project.task'

#     name = fields.Char(string='Nombre', required=True)
#     proyecto_id = fields.Many2one('mi_modulo.proyecto', string='Proyecto')
#     subtareas_ids = fields.One2many('mi_modulo.subtarea', 'tarea_id', string='Subtareas')

# class Subtarea(models.Model):
#     _name = 'project.task'
#     _description = 'Subtareas'
#     _inherit = 'project.task'

#     name = fields.Char(string='Nombre', required=True)
#     tarea_id = fields.Many2one('mi_modulo.tarea', string='Tarea')


# class ResUsers(models.Model):
#     _inherit = 'res.users'

#     is_admin = fields.Boolean(string='Es Administrador')
#     is_jefe_proyecto = fields.Boolean(string='Es Jefe de Proyecto')
#     is_analista = fields.Boolean(string='Es Analista')
#     is_programador = fields.Boolean(string='Es Programador')

