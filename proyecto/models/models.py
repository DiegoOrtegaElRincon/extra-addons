# models.py
from odoo import models, fields, api

class EmpresaContratista(models.Model):
    _name = 'mi_modulo.empresa_contratista'
    _description = 'Empresas contratistas'

    name = fields.Char(string='Nombre', required=True)
    proyectos_ids = fields.One2many('mi_modulo.proyecto', 'contratista_id', string='Proyectos')
 
class Proyecto(models.Model):
    _name = 'mi_modulo.proyecto'
    _description = 'Proyectos'
    _inherit = 'project.project'

    contratista_id = fields.Many2one('mi_modulo.empresa_contratista', string='Contratista')
    tareas_ids = fields.One2many('mi_modulo.tarea', 'proyecto_id', string='Tareas')
    total_tareas = fields.Integer(string='Total de Tareas', compute='_compute_total_tareas', store=True)
    
    @api.depends('tareas_ids')
    def _compute_total_tareas(self):
        for proyecto in self:
            proyecto.total_tareas = len(proyecto.tareas_ids)

class Tarea(models.Model):
    _name = 'mi_modulo.tarea' 
    _description = 'Tareas'
    _inherit = 'project.task'

    name = fields.Char(string='Nombre', required=True)
    proyecto_id = fields.Many2one('mi_modulo.proyecto', string='Proyecto')
    subtareas_ids = fields.One2many('mi_modulo.subtarea', 'tarea_id', string='Subtareas')

class Subtarea(models.Model):
    _name = 'project.task'
    _description = 'Subtareas'
    _inherit = 'project.task'

    name = fields.Char(string='Nombre', required=True)
    tarea_id = fields.Many2one('mi_modulo.tarea', string='Tarea')


class ResUsers(models.Model):
    _inherit = 'res.users'

    is_admin = fields.Boolean(string='Es Administrador')
    is_jefe_proyecto = fields.Boolean(string='Es Jefe de Proyecto')
    is_analista = fields.Boolean(string='Es Analista')
    is_programador = fields.Boolean(string='Es Programador')

