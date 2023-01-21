const Pool = require("pg").Pool;

const DB_USER = process.env.DB_USER ?? "postgres";
const DB_HOST = process.env.DB_HOST ?? "localhost";
const DB_DATABASE = process.env.DB_DATABASE ?? "ssluzba";
const DB_PASSWORD = process.env.DB_PASSWORD ?? "123";
const DB_PORT = process.env.PORT ?? 5432;

const pool = new Pool({
  user: DB_USER,
  host: DB_HOST,
  database: DB_DATABASE,
  password: DB_PASSWORD,
  port: DB_PORT,
});

const createProfessor = (request, response) => {
  const user = request.body;
  console.log("nesto ne stima ovdje");
  createUser(user, "PROFESSOR", response);
};
const createStudent = (request, response) => {
  const user = request.body;
  createUser(user, "STUDENT", response);
};

function createUser(user, user_type, response) {
  pool.query(
    "INSERT INTO users (name, jmbg, type) VALUES ($1,$2,$3) RETURNING *",
    [user.name, user.jmbg, user_type],
    (error, result) => {
      if (error) {
        response
          .status(500)
          .send(`${user_type} sa JMBG: ${user.jmbg} vec postoji!`);
      } else {
        response
          .status(201)
          .send(`${user_type} sa JMBG: ${user.jmbg} uspesno kreiran!`);
      }
    }
  );
}

module.exports = {
  createProfessor,
  createStudent,
};
