FROM node:24-alpine AS build

RUN corepack enable && corepack prepare pnpm@11.21.0 --activate
WORKDIR /app

COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./
RUN pnpm install --frozen-lockfile

COPY tsconfig.json tsconfig.build.json ./
COPY src ./src
RUN pnpm build

FROM node:24-alpine AS runtime

WORKDIR /app
COPY --from=build /app/package.json ./package.json
COPY --from=build /app/dist ./dist

USER node
ENTRYPOINT ["node", "dist/cli.js"]
CMD ["--help"]
