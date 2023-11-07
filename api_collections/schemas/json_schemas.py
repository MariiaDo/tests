class NotesSchema:
    all_notes = {
        "type": "object",
        "properties": {
            "success": {
                "type": "boolean"
            },
            "status": {
                "type": "number"
            },
            "message": {
                "type": "string"
            },
            "data": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string"
                        },
                        "title": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        },
                        "category": {
                            "type": "string"
                        },
                        "completed": {
                            "type": "boolean"
                        },
                        "created_at": {
                            "type": "string"
                        },
                        "updated_at": {
                            "type": "string"
                        },
                        "user_id": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "id",
                        "title",
                        "description",
                        "category",
                        "completed",
                        "created_at",
                        "updated_at",
                        "user_id"
                    ]
                }
            }
        },
        "required": [
            "success",
            "status",
            "message",
            "data"
        ]
    }
    get_note_by_id = {
        "type": "object",
        "properties": {
            "success": {
                "type": "boolean"
            },
            "status": {
                "type": "number"
            },
            "message": {
                "type": "string"
            },
            "data": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string"
                    },
                    "title": {
                        "type": "string"
                    },
                    "description": {
                        "type": "string"
                    },
                    "category": {
                        "type": "string"
                    },
                    "completed": {
                        "type": "boolean"
                    },
                    "created_at": {
                        "type": "string"
                    },
                    "updated_at": {
                        "type": "string"
                    },
                    "user_id": {
                        "type": "string"
                    }
                },
                "required": [
                    "id",
                    "title",
                    "description",
                    "category",
                    "completed",
                    "created_at",
                    "updated_at",
                    "user_id"
                ]
            }
        },
        "required": [
            "success",
            "status",
            "message",
            "data"
        ]
    }
    post_new_note = {
        "type": "object",
        "properties": {
            "success": {
                "type": "boolean"
            },
            "status": {
                "type": "number"
            },
            "message": {
                "type": "string"
            },
            "data": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string"
                    },
                    "title": {
                        "type": "string"
                    },
                    "description": {
                        "type": "string"
                    },
                    "category": {
                        "type": "string"
                    },
                    "completed": {
                        "type": "boolean"
                    },
                    "created_at": {
                        "type": "string"
                    },
                    "updated_at": {
                        "type": "string"
                    },
                    "user_id": {
                        "type": "string"
                    }
                },
                "required": [
                    "id",
                    "title",
                    "description",
                    "category",
                    "completed",
                    "created_at",
                    "updated_at",
                    "user_id"
                ]
            }
        },
        "required": [
            "success",
            "status",
            "message",
            "data"
        ]
    }
    put_notes_by_id = {
        "type": "object",
        "properties": {
            "success": {
                "type": "boolean"
            },
            "status": {
                "type": "number"
            },
            "message": {
                "type": "string"
            },
            "data": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string"
                    },
                    "title": {
                        "type": "string"
                    },
                    "description": {
                        "type": "string"
                    },
                    "category": {
                        "type": "string"
                    },
                    "completed": {
                        "type": "boolean"
                    },
                    "created_at": {
                        "type": "string"
                    },
                    "updated_at": {
                        "type": "string"
                    },
                    "user_id": {
                        "type": "string"
                    }
                },
                "required": [
                    "id",
                    "title",
                    "description",
                    "category",
                    "completed",
                    "created_at",
                    "updated_at",
                    "user_id"
                ]
            }
        },
        "required": [
            "success",
            "status",
            "message",
            "data"
        ]
    }
    patch_completed_by_id = {
        "type": "object",
        "properties": {
            "success": {
                "type": "boolean"
            },
            "status": {
                "type": "number"
            },
            "message": {
                "type": "string"
            },
            "data": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string"
                    },
                    "title": {
                        "type": "string"
                    },
                    "description": {
                        "type": "string"
                    },
                    "category": {
                        "type": "string"
                    },
                    "completed": {
                        "type": "boolean"
                    },
                    "created_at": {
                        "type": "string"
                    },
                    "updated_at": {
                        "type": "string"
                    },
                    "user_id": {
                        "type": "string"
                    }
                },
                "required": [
                    "id",
                    "title",
                    "description",
                    "category",
                    "completed",
                    "created_at",
                    "updated_at",
                    "user_id"
                ]
            }
        },
        "required": [
            "success",
            "status",
            "message",
            "data"
        ]
    }
    delete_note_by_id = {
        "type": "object",
        "properties": {
            "success": {
                "type": "boolean"
            },
            "status": {
                "type": "number"
            },
            "message": {
                "type": "string"
            }
        },
        "required": [
            "success",
            "status",
            "message"
        ]
    }

