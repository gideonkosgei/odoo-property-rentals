/** @odoo-module **/
import { registry } from "@web/core/registry";
import { KanbanView } from "@web/views/kanban/kanban_view";

export class HrEmployeeKanban extends KanbanView {}

registry.category("views").add("hr_employee_kanban", HrEmployeeKanban);

