# models.py
from odoo import models, fields, api

class EmpresaContratista(models.Model):
    _name = 'empresa_contratista'
    _description = 'Empresas Contratistas'

    name = fields.Char(string='Nombre', required=True)
    direccion = fields.Char(string='Direccion', required=True)
    display_info = fields.Char(string='Display Info', compute='_compute_display_info')
    proyectos = fields.Many2many("project.project",string="Proyectos")

    @api.depends('name', 'direccion')
    def _compute_display_info(self):
        for record in self:
            record.display_info = "{} - {}".format(record.name, record.direccion)
 
class Proyecto(models.Model):
    _name = 'project.project'
    _inherit = 'project.project'

    empresas_contratistas = fields.Many2one("empresas_contratistas",string="Empresa Contratista",inverse_name='proyectos')
    # tareas_ids = fields.One2many('project.task', 'project_id', string='Tareas')
    # total_tareas = fields.Integer(string='Total de Tareas', compute='_compute_total_tareas', store=True)
    
    # @api.depends('tareas_ids')
    # def _compute_total_tareas(self):
    #     for proyecto in self:
    #         proyecto.total_tareas = len(proyecto.tareas_ids)

# class Tarea(models.Model):
#     _name = 'project.task'
#     _inherit = 'project.task'

#     proyecto_id = fields.Many2one('proyecto', string='Proyecto')


