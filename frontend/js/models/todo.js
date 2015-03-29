app.models.todo = Backbone.Model.extend({
    defaults: {
        title: "Todo",
        archived: false,
        done: false
    }
});
