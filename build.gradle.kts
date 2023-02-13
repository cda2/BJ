import org.jetbrains.kotlin.gradle.dsl.JvmTarget
import org.jetbrains.kotlin.gradle.tasks.KotlinCompile

plugins {
    kotlin("jvm") version "1.8.10"
    application
}

group = "com.cda2"

version = "1.0-SNAPSHOT"

repositories { mavenCentral() }

dependencies {
    testImplementation(kotlin("test"))
    testImplementation(kotlin("test-junit5"))
    testImplementation("org.junit.jupiter:junit-jupiter-params:+")
    testImplementation("org.assertj:assertj-core:+")
    testImplementation("io.kotest:kotest-runner-junit5:+")
    testImplementation("io.kotest:kotest-framework-datatest:+")
    implementation(kotlin("stdlib-jdk8"))
}

tasks.test { useJUnitPlatform() }

tasks.withType<KotlinCompile> { compilerOptions.jvmTarget.set(JvmTarget.JVM_17) }

application { mainClass.set("MainKt") }

val compileKotlin: KotlinCompile by tasks

compileKotlin.kotlinOptions { jvmTarget = "17" }

val compileTestKotlin: KotlinCompile by tasks

compileTestKotlin.kotlinOptions { jvmTarget = "17" }
