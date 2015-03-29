app.views.menu = Backbone.View.extend({
    templates: _.template($("tpl-menu").html()),
    initialize: function() {
        this.render(); 
    },
    render: function() {
        this.$el.html(this.template({}));
    }
});

