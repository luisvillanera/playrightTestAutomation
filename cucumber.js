module.exports = {
  default: {
    requireModule: ['ts-node/register'],
    require: ['src/steps/*.ts', 'src/hooks/*.ts'],
    format: ['progress-bar', 'html:cucumber-report.html'],
    paths: ['src/features/'],
    publishQuiet: true
  }
} 