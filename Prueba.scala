import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._

class MySimulation extends Simulation {

  val httpConf = http
    .baseUrl("http://localhost:5000") //Url de la app Flask, por default esta en este puerto
    .acceptHeader("application/json")

  val scn = scenario("Enviar JSON a Flask")
    .exec(http("POST JSON")
      .post("/prueba")
      .body(StringBody("""{
        "animales": [
          {
            "Tipo": "Perro",
            "Nombre": "Max"
          },
          {
            "Tipo": "Gato",
            "Nombre": "Manchas"
          },
          {
            "Tipo": "Perro",
            "Nombre": "Bruno"
          }
        ]
      }""")).asJson
      .check(status.is(200)))

  setUp(
    scn.inject(
      constantUsersPerSec(1) during (1 seconds) //Cantidad de usuarios por segundo que van a realizar peticiones
    )
  ).protocols(httpConf)

}