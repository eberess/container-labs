const { Sequelize, DataTypes } = require('sequelize');

const sequelize = new Sequelize(process.env.DB_NAME, process.env.DB_USER, process.env.DB_PASS, {
  host: process.env.DB_HOST,
  dialect: 'postgres',
});

const db = {};

db.sequelize = sequelize;
db.Sequelize = Sequelize;

db.posts = require('./post.js')(sequelize, DataTypes);
db.comments = require('./comment.js')(sequelize, DataTypes);

// Définition des relations
db.posts.hasMany(db.comments, {
  onDelete: 'CASCADE',
});
db.comments.belongsTo(db.posts);

module.exports = db;
