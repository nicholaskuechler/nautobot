from nautobot.core.apps import (
    NavContext,
    NavGrouping,
    NavItem,
    NavMenuAddButton,
    NavMenuGroup,
    NavMenuItem,
    NavMenuImportButton,
    NavMenuTab,
)


menu_items = (
    NavMenuTab(
        name="Organization",
        weight=100,
        groups=(
            NavMenuGroup(
                name="Tags",
                weight=400,
                items=(
                    NavMenuItem(
                        link="extras:tag_list",
                        name="Tags",
                        weight=100,
                        permissions=[
                            "extras.view_tag",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="extras:tag_add",
                                permissions=[
                                    "extras.add_tag",
                                ],
                            ),
                            NavMenuImportButton(
                                link="extras:tag_import",
                                permissions=[
                                    "extras.add_tag",
                                ],
                            ),
                        ),
                    ),
                ),
            ),
            NavMenuGroup(
                name="Statuses",
                weight=500,
                items=(
                    NavMenuItem(
                        link="extras:status_list",
                        name="Statuses",
                        weight=100,
                        permissions=[
                            "extras.view_status",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="extras:status_add",
                                permissions=[
                                    "extras.add_status",
                                ],
                            ),
                            NavMenuImportButton(
                                link="extras:status_import",
                                permissions=[
                                    "extras.add_status",
                                ],
                            ),
                        ),
                    ),
                ),
            ),
            NavMenuGroup(
                name="Roles",
                weight=500,
                items=(
                    NavMenuItem(
                        link="extras:role_list",
                        name="Roles",
                        weight=100,
                        permissions=[
                            "extras.view_status",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="extras:role_add",
                                permissions=[
                                    "extras.add_role",
                                ],
                            ),
                            NavMenuImportButton(
                                link="extras:role_import",
                                permissions=[
                                    "extras.add_role",
                                ],
                            ),
                        ),
                    ),
                ),
            ),
            NavMenuGroup(
                name="Dynamic Groups",
                weight=500,
                items=(
                    NavMenuItem(
                        link="extras:dynamicgroup_list",
                        name="Dynamic Groups",
                        weight=100,
                        permissions=[
                            "extras.view_dynamicgroup",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="extras:dynamicgroup_add",
                                permissions=[
                                    "extras.add_dynamicgroup",
                                ],
                            ),
                        ),
                    ),
                ),
            ),
        ),
    ),
    NavMenuTab(
        name="Secrets",
        weight=700,
        groups=(
            NavMenuGroup(
                name="Secrets",
                weight=100,
                items=(
                    NavMenuItem(
                        link="extras:secret_list",
                        name="Secrets",
                        weight=100,
                        permissions=["extras.view_secret"],
                        buttons=(
                            NavMenuAddButton(link="extras:secret_add", permissions=["extras.add_secret"]),
                            NavMenuImportButton(link="extras:secret_import", permissions=["extras.add_secret"]),
                        ),
                    ),
                    NavMenuItem(
                        link="extras:secretsgroup_list",
                        name="Secret Groups",
                        weight=200,
                        permissions=["extras.view_secretsgroup"],
                        buttons=(
                            NavMenuAddButton(link="extras:secretsgroup_add", permissions=["extras.add_secretsgroup"]),
                        ),
                    ),
                ),
            ),
        ),
    ),
    NavMenuTab(
        name="Jobs",
        weight=800,
        groups=(
            NavMenuGroup(
                name="Jobs",
                weight=100,
                items=(
                    NavMenuItem(
                        link="extras:job_list",
                        name="Jobs",
                        weight=100,
                        permissions=[
                            "extras.view_job",
                        ],
                        buttons=(),
                    ),
                    NavMenuItem(
                        link="extras:scheduledjob_approval_queue_list",
                        name="Job Approval Queue",
                        weight=200,
                        permissions=[
                            "extras.view_job",
                        ],
                        buttons=(),
                    ),
                    NavMenuItem(
                        link="extras:scheduledjob_list",
                        name="Scheduled Jobs",
                        weight=300,
                        permissions=[
                            "extras.view_job",
                            "extras.view_scheduledjob",
                        ],
                        buttons=(),
                    ),
                    NavMenuItem(
                        link="extras:jobresult_list",
                        name="Job Results",
                        weight=400,
                        permissions=[
                            "extras.view_jobresult",
                        ],
                        buttons=(),
                    ),
                    NavMenuItem(
                        link="extras:jobhook_list",
                        name="Job Hooks",
                        weight=500,
                        permissions=[
                            "extras.view_jobhook",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="extras:jobhook_add",
                                permissions=[
                                    "extras.add_jobhook",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="extras:jobbutton_list",
                        name="Job Buttons",
                        weight=600,
                        permissions=[
                            "extras.view_jobbutton",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="extras:jobbutton_add",
                                permissions=[
                                    "extras.add_jobbutton",
                                ],
                            ),
                        ),
                    ),
                ),
            ),
        ),
    ),
    NavMenuTab(
        name="Extensibility",
        weight=900,
        groups=(
            NavMenuGroup(
                name="Logging",
                weight=100,
                items=(
                    NavMenuItem(
                        link="extras:objectchange_list",
                        name="Change Log",
                        weight=100,
                        permissions=[
                            "extras.view_objectchange",
                        ],
                        buttons=(),
                    ),
                ),
            ),
            NavMenuGroup(
                name="Data Sources",
                weight=200,
                items=(
                    NavMenuItem(
                        link="extras:gitrepository_list",
                        name="Git Repositories",
                        weight=100,
                        permissions=[
                            "extras.view_gitrepository",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="extras:gitrepository_add",
                                permissions=[
                                    "extras.add_gitrepository",
                                ],
                            ),
                            NavMenuImportButton(
                                link="extras:gitrepository_import",
                                permissions=[
                                    "extras.add_gitrepository",
                                ],
                            ),
                        ),
                    ),
                ),
            ),
            NavMenuGroup(
                name="Data Management",
                weight=300,
                items=(
                    NavMenuItem(
                        link="extras:graphqlquery_list",
                        name="GraphQL Queries",
                        weight=100,
                        permissions=[
                            "extras.view_graphqlquery",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="extras:graphqlquery_add",
                                permissions=[
                                    "extras.add_graphqlquery",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="extras:relationship_list",
                        name="Relationships",
                        weight=200,
                        permissions=[
                            "extras.view_relationship",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="extras:relationship_add",
                                permissions=[
                                    "extras.add_relationship",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="extras:note_list",
                        name="Notes",
                        weight=300,
                        permissions=[
                            "extras.view_note",
                        ],
                    ),
                ),
            ),
            NavMenuGroup(
                name="Automation",
                weight=500,
                items=(
                    NavMenuItem(
                        link="extras:configcontext_list",
                        name="Config Contexts",
                        weight=100,
                        permissions=[
                            "extras.view_configcontext",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="extras:configcontext_add",
                                permissions=[
                                    "extras.add_configcontext",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="extras:configcontextschema_list",
                        name="Config Context Schemas",
                        weight=100,
                        permissions=[
                            "extras.view_configcontextschema",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="extras:configcontextschema_add",
                                permissions=[
                                    "extras.add_configcontextschema",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="extras:exporttemplate_list",
                        name="Export Templates",
                        weight=200,
                        permissions=[
                            "extras.view_exporttemplate",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="extras:exporttemplate_add",
                                permissions=[
                                    "extras.add_exporttemplate",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="extras:webhook_list",
                        name="Webhooks",
                        weight=400,
                        permissions=[
                            "extras.view_webhook",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="extras:webhook_add",
                                permissions=[
                                    "extras.add_webhook",
                                ],
                            ),
                        ),
                    ),
                ),
            ),
            NavMenuGroup(
                name="Miscellaneous",
                weight=600,
                items=(
                    NavMenuItem(
                        link="extras:computedfield_list",
                        name="Computed Fields",
                        weight=100,
                        permissions=[
                            "extras.view_computedfield",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="extras:computedfield_add",
                                permissions=[
                                    "extras.add_computedfield",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="extras:customfield_list",
                        name="Custom Fields",
                        weight=200,
                        permissions=[
                            "extras.view_customfield",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="extras:customfield_add",
                                permissions=[
                                    "extras.add_customfield",
                                ],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="extras:customlink_list",
                        name="Custom Links",
                        weight=300,
                        permissions=[
                            "extras.view_customlink",
                        ],
                        buttons=(
                            NavMenuAddButton(
                                link="extras:customlink_add",
                                permissions=[
                                    "extras.add_customlink",
                                ],
                            ),
                        ),
                    ),
                ),
            ),
        ),
    ),
    NavMenuTab(
        name="Plugins",
        weight=5000,
        groups=(
            NavMenuGroup(
                name="General",
                weight=100,
                items=(
                    NavMenuItem(
                        link="plugins:plugins_list",
                        name="Installed Plugins",
                        weight=100,
                        permissions=["is_staff"],
                        buttons=(),
                    ),
                ),
            ),
        ),
    ),
)


navigation = (
    NavContext(
        name="Inventory",
        groups=(
            NavGrouping(
                name="Devices",
                weight=100,
                items=(
                    NavItem(
                        name="Dynamic Groups",
                        weight=900,
                        link="extras:dynamicgroup_list",
                        permissions=["extras.view_dynamicgroup"],
                    ),
                ),
            ),
        ),
    ),
    NavContext(
        name="Networks",
        groups=(
            NavGrouping(
                name="Config Contexts",
                weight=500,
                items=(
                    NavItem(
                        name="Config Contexts",
                        weight=100,
                        link="extras:configcontext_list",
                        permissions=["extras.view_configcontext"],
                    ),
                    NavItem(
                        name="Config Context Schemas",
                        weight=100,
                        link="extras:configcontextschema_list",
                        permissions=["extras.view_configcontextschema"],
                    ),
                ),
            ),
        ),
    ),
    NavContext(
        name="Security",
        groups=(
            NavGrouping(
                name="Secrets",
                weight=500,
                items=(
                    NavItem(
                        name="Secrets",
                        weight=100,
                        link="extras:secret_list",
                        permissions=["extras.view_secret"],
                    ),
                    NavItem(
                        name="Secret Groups",
                        weight=200,
                        link="extras:secretsgroup_list",
                        permissions=["extras.view_secretsgroup"],
                    ),
                ),
            ),
        ),
    ),
    NavContext(
        name="Automation",
        groups=(
            NavGrouping(
                name="Jobs",
                weight=100,
                items=(
                    NavItem(
                        link="extras:job_list",
                        name="Jobs",
                        weight=100,
                        permissions=[
                            "extras.view_job",
                        ],
                    ),
                    NavItem(
                        link="extras:scheduledjob_approval_queue_list",
                        name="Job Approval Queue",
                        weight=200,
                        permissions=[
                            "extras.view_job",
                        ],
                    ),
                    NavItem(
                        link="extras:scheduledjob_list",
                        name="Scheduled Jobs",
                        weight=300,
                        permissions=[
                            "extras.view_job",
                            "extras.view_scheduledjob",
                        ],
                    ),
                    NavItem(
                        link="extras:jobresult_list",
                        name="Job Results",
                        weight=400,
                        permissions=[
                            "extras.view_jobresult",
                        ],
                    ),
                    NavItem(
                        link="extras:jobhook_list",
                        name="Job Hooks",
                        weight=500,
                        permissions=[
                            "extras.view_jobhook",
                        ],
                    ),
                    NavItem(
                        link="extras:jobbutton_list",
                        name="Job Buttons",
                        weight=600,
                        permissions=[
                            "extras.view_jobbutton",
                        ],
                    ),
                ),
            ),
            NavGrouping(
                name="Extensibility",
                weight=9999,  # always last
                items=(
                    NavItem(
                        link="extras:webhook_list",
                        name="Webhooks",
                        weight=100,
                        permissions=["extras.view_webhook"],
                    ),
                    NavItem(
                        name="GraphQL Queries",
                        weight=200,
                        link="extras:graphqlquery_list",
                        permissions=["extras.view_graphqlquery"],
                    ),
                    NavItem(
                        name="Export Templates",
                        weight=300,
                        link="extras:exporttemplate_list",
                        permissions=["extras.view_exporttemplate"],
                    ),
                ),
            ),
        ),
    ),
    NavContext(
        name="Platform",
        groups=(
            NavGrouping(
                name="Platform",
                weight=100,
                items=(
                    NavItem(
                        name="Installed Apps",
                        weight=100,
                        link="plugins:plugins_list",
                        permissions=["is_staff"],
                    ),
                    NavItem(
                        name="Git Repositories",
                        weight=200,
                        link="extras:gitrepository_list",
                        permissions=["extras.view_gitrepository"],
                    ),
                ),
            ),
            NavGrouping(
                name="Governance",
                weight=200,
                items=(
                    NavItem(
                        name="Change Log",
                        weight=100,
                        link="extras:objectchange_list",
                        permissions=["extras.view_objectchange"],
                    ),
                ),
            ),
            NavGrouping(
                name="Reference Data",
                weight=300,
                items=(
                    NavItem(
                        name="Tags",
                        weight=100,
                        link="extras:tag_list",
                        permissions=["extras.view_tag"],
                    ),
                    NavItem(
                        name="Statuses",
                        weight=200,
                        link="extras:status_list",
                        permissions=["extras.view_status"],
                    ),
                    NavItem(
                        name="Roles",
                        weight=300,
                        link="extras:role_list",
                        permissions=["extras.view_role"],
                    ),
                ),
            ),
            NavGrouping(
                name="Data Management",
                weight=400,
                items=(
                    NavItem(
                        name="Relationships",
                        weight=100,
                        link="extras:relationship_list",
                        permissions=["extras.view_relationship"],
                    ),
                    NavItem(
                        name="Computed Fields",
                        weight=200,
                        link="extras:computedfield_list",
                        permissions=["extras.view_computedfield"],
                    ),
                    NavItem(
                        name="Custom Fields",
                        weight=300,
                        link="extras:customfield_list",
                        permissions=["extras.view_customfield"],
                    ),
                    NavItem(
                        name="Custom Links",
                        weight=400,
                        link="extras:customlink_list",
                        permissions=["extras.view_customlink"],
                    ),
                    NavItem(
                        name="Notes",
                        weight=500,
                        # TODO figure out what link we should put here
                        # This NavItem is required for the breadCrumb on NotesDetailView to render.
                        # However `extras:note_list` is not a reverse url lookup that does not exist.
                        link="extras:note_list",
                        permissions=["extras.view_note"],
                    ),
                ),
            ),
        ),
    ),
)
