//REVISAR COMENTARIOS

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._

class MariaDB extends Simulation {

  val httpConf = http
    .baseUrl("http://localhost:30000") //Url de la app Flask
    .acceptHeader("application/json")

  val scn = scenario("Enviar JSON a Flask")
    .exec(http("POST JSON")
      .post("/mariadb/post") //La ruta donde se nececita enviar la informacion
      .body(StringBody("""{"query":"select",
			"host": "(es el cluster ip de la base de datos mariadb)"}""")).asJson
      .check(status.is(200)))

  setUp(
    scn.inject(
      constantUsersPerSec(1) during (1 seconds) //Cantidad de usuarios por intervalo de tiempo que realizaran las peticiones
    )
  ).protocols(httpConf)

}